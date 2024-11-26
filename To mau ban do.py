from simpleai.search import CspProblem, backtrack 

# Hàm ràng buộc: kiểm tra xem hai miền có khác màu nhau không
def constraint_func(names, values):
    return values[0] != values[1]

# Tự tô màu cho bản đồ miền tây
if __name__ == '__main__':
    # Danh sách các khu vực
    names = ('WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T')
    
    # Miền giá trị cho từng khu vực
    domain = {
        'WA':  ['R', 'G', 'B'],
        'NT':  ['R', 'G', 'B'],
        'Q':   ['R', 'G', 'B'],
        'NSW': ['R', 'G', 'B'],
        'V':   ['R', 'G', 'B'],
        'SA':  ['R', 'G', 'B'],
        'T':   ['R', 'G', 'B'],
    }

    # Các ràng buộc: các khu vực liền kề không được cùng màu
    constraints = [
        (('SA', 'WA'), constraint_func),
        (('SA', 'NT'), constraint_func),
        (('SA', 'Q'), constraint_func),
        (('SA', 'NSW'), constraint_func),
        (('SA', 'V'), constraint_func),
        (('WA', 'NT'), constraint_func),
        (('NT', 'Q'), constraint_func),
        (('Q', 'NSW'), constraint_func),
        (('NSW', 'V'), constraint_func),
    ]

    # Định nghĩa bài toán và tìm giải pháp
    problem = CspProblem(names, domain, constraints)
    output = backtrack(problem)
    
    # In kết quả
    print("Giải pháp tô màu:", output)
