import torch
import torch.nn as nn
import torch.optim as optim
import math

from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

##############################################################################
# 1. Example Data
##############################################################################
train_data = [
    ("hello world", "hola mundo"),
    ("how are you", "como estas"),
    ("i love pytorch", "me encanta pytorch"),
    ("this is a book", "esto es un libro"),
]

##############################################################################
# 2. Tokenizers and Vocab
##############################################################################
en_tokenizer = get_tokenizer('spacy', language='en_core_web_sm')
es_tokenizer = get_tokenizer('spacy', language='es_core_news_sm')

def yield_tokens(data, en_tok, es_tok):
    """Combine English and Spanish tokens into a single vocabulary for simplicity."""
    for eng, _ in data:
        yield en_tok(eng)
    for _, spa in data:
        yield es_tok(spa)

vocab = build_vocab_from_iterator(
    yield_tokens(train_data, en_tokenizer, es_tokenizer),
    specials=['<unk>', '<pad>', '<bos>', '<eos>']
)
vocab.set_default_index(vocab['<unk>'])

PAD_IDX = vocab['<pad>']
BOS_IDX = vocab['<bos>']
EOS_IDX = vocab['<eos>']

##############################################################################
# 3. Data Preparation
##############################################################################
def text_to_tensor(text, tokenizer, vocab):
    return [vocab[token] for token in tokenizer(text)]

def collate_fn(batch):
    src_batch = []
    tgt_batch = []
    for eng, spa in batch:
        src = text_to_tensor(eng, en_tokenizer, vocab)
        tgt = text_to_tensor(spa, es_tokenizer, vocab)
        src_batch.append(torch.tensor(src, dtype=torch.long))
        tgt_batch.append(torch.tensor([BOS_IDX] + tgt + [EOS_IDX], dtype=torch.long))

    # pad_sequence gives shape [max_seq_len, batch_size]
    src_batch = nn.utils.rnn.pad_sequence(src_batch, padding_value=PAD_IDX)
    tgt_batch = nn.utils.rnn.pad_sequence(tgt_batch, padding_value=PAD_IDX)
    return src_batch, tgt_batch

train_dataloader = torch.utils.data.DataLoader(
    train_data, 
    batch_size=2,
    shuffle=True, 
    collate_fn=collate_fn
)

##############################################################################
# 4. Positional Encoding
##############################################################################
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout=0.1, max_len=5000):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(1)  # shape => [max_len, 1, d_model]
        self.register_buffer('pe', pe)

    def forward(self, x):
        # x => [seq_len, batch_size, d_model]
        x = x + self.pe[:x.size(0), :]
        return self.dropout(x)

##############################################################################
# 5. Transformer Model
##############################################################################
class Seq2SeqTransformer(nn.Module):
    def __init__(self, vocab_size, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model, dropout)

        self.transformer = nn.Transformer(
            d_model=d_model,
            nhead=nhead,
            num_encoder_layers=num_encoder_layers,
            num_decoder_layers=num_decoder_layers,
            dim_feedforward=dim_feedforward,
            dropout=dropout
        )
        self.fc_out = nn.Linear(d_model, vocab_size)

    def forward(self, src, tgt):
        # src, tgt => [seq_len, batch_size]
        src_emb = self.pos_encoder(self.embedding(src) * math.sqrt(self.d_model))
        tgt_emb = self.pos_encoder(self.embedding(tgt) * math.sqrt(self.d_model))

        # Generate causal mask for the target sequence
        tgt_seq_len, _ = tgt.size()
        tgt_mask = nn.Transformer.generate_square_subsequent_mask(tgt_seq_len).to(device)

        # Run through the transformer
        output = self.transformer(
            src_emb, 
            tgt_emb, 
            tgt_mask=tgt_mask
            # For real tasks, also pass src_key_padding_mask, tgt_key_padding_mask, etc.
        )
        # output => [seq_len, batch_size, d_model]
        logits = self.fc_out(output)  # => [seq_len, batch_size, vocab_size]
        return logits

##############################################################################
# 6. Initialize Model and Optimizer
##############################################################################
vocab_size = len(vocab)
d_model = 256
nhead = 8
num_encoder_layers = 3
num_decoder_layers = 3
dim_feedforward = 512

model = Seq2SeqTransformer(
    vocab_size=vocab_size,
    d_model=d_model,
    nhead=nhead,
    num_encoder_layers=num_encoder_layers,
    num_decoder_layers=num_decoder_layers,
    dim_feedforward=dim_feedforward,
    dropout=0.1
).to(device)

criterion = nn.CrossEntropyLoss(ignore_index=PAD_IDX)
optimizer = optim.Adam(model.parameters(), lr=0.001)

##############################################################################
# 7. Training Loop
##############################################################################
def train_epoch(model, dataloader, optimizer, criterion):
    model.train()
    total_loss = 0
    for src, tgt in dataloader:
        src, tgt = src.to(device), tgt.to(device)

        # The model needs:
        #   - Decoder inputs (tgt_input): all but the last token 
        #   - Labels (tgt_output): all but the first token
        tgt_input = tgt[:-1, :]
        tgt_output = tgt[1:, :]

        optimizer.zero_grad()
        logits = model(src, tgt_input)
        # Flatten logits and labels for cross-entropy
        logits_flat = logits.view(-1, logits.size(-1))
        tgt_output_flat = tgt_output.view(-1)

        loss = criterion(logits_flat, tgt_output_flat)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    return total_loss / len(dataloader)

EPOCHS = 20
for epoch in range(EPOCHS):
    epoch_loss = train_epoch(model, train_dataloader, optimizer, criterion)
    print(f"Epoch {epoch+1}, Loss: {epoch_loss:.4f}")

##############################################################################
# 8. Translation (Greedy Decode)
##############################################################################
def greedy_decode(model, src, max_len=20):
    model.eval()
    src = src.to(device)

    # Encode source
    src_emb = model.pos_encoder(model.embedding(src) * math.sqrt(model.d_model))
    memory = model.transformer.encoder(src_emb)

    # Start token
    ys = torch.tensor([[BOS_IDX]], dtype=torch.long, device=device)

    for _ in range(max_len):
        tgt_emb = model.pos_encoder(model.embedding(ys) * math.sqrt(model.d_model))
        tgt_mask = nn.Transformer.generate_square_subsequent_mask(ys.size(0)).to(device)
        out = model.transformer.decoder(tgt_emb, memory, tgt_mask=tgt_mask)
        out = model.fc_out(out)  # [tgt_seq_len, 1, vocab_size]
        next_word = torch.argmax(out[-1, 0, :]).item()
        ys = torch.cat([ys, torch.tensor([[next_word]], device=device)], dim=0)
        if next_word == EOS_IDX:
            break
    return ys

def translate_sentence(model, sentence):
    tokens = [vocab[token] for token in en_tokenizer(sentence)]
    src = torch.tensor(tokens, dtype=torch.long).unsqueeze(1).to(device)
    tgt_tokens = greedy_decode(model, src)
    # Convert IDs back to tokens and remove <bos> / <eos> for readability
    raw_tokens = vocab.lookup_tokens(tgt_tokens.squeeze().tolist())
    # Trim from <bos> up to <eos>
    if '<bos>' in raw_tokens:
        raw_tokens.remove('<bos>')
    if '<eos>' in raw_tokens:
        raw_tokens.remove('<eos>')
    return ' '.join(raw_tokens)

##############################################################################
# 9. Quick Test
##############################################################################
test_sentences = [
    "hello world",
    "this is a book",
    "how are you",
]

for s in test_sentences:
    translation = translate_sentence(model, s)
    print(f"{s} -> {translation}")
