line_num = 0
with open('/home/alex/Documents/SoftUni/open_courses/python/lecture-4/catalog_sample.csv') as catalog:
    for line in catalog:
        print(line_num)
        line_num += 1