for i in range(800):
    with open(f"../datasets/cruxeval_new_test/sample_{i}_f.py","r",encoding="utf-8") as f:
        code = f.read()
        code += "\ntest_check()"
    globals_dict = {}
    # try:
        # 执行代码以定义函数
    exec(code, globals_dict)
    # except:
    #     print(f"../datasets/cruxeval_new_test/sample_{i}_f.py")
