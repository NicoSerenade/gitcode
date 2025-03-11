def get_total_classes(classes_per_week, weeks, no_class_days):
    total_classes = (classes_per_week * weeks) - no_class_days
    return total_classes


def get_max_allowable_absences(classes_per_week,weeks,no_class_days,allowable_percentage):
    total_classes = get_total_classes(classes_per_week, weeks, no_class_days)

    get_max_allowable_absences = total_classes*allowable_percentage
    return round(get_max_allowable_absences)