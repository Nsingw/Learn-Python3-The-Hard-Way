import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):  #main函数主体，后调用
    line = language_file.readline()  #从给出的languages文件读取一行

    if line:  #若line不为空字符串时执行，当readline函数到达文件末尾的时候，它会返回空字符串
        print_line(line, encoding, errors)  #调用print打印 编码languages.txt文件中的每一行内容
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()  #用于移除字符串头尾指定字符（默认为空格）或字符序列
    raw_bytes = next_lang.encode(encoding, errors = errors)  #编码字符串，获得原始字节，就是把想要的编码以及如何处理错误传递给encode()
    cooked_string = raw_bytes.decode(encoding, errors = errors)  #raw_bytes是字节，调用decode()来获取字符串

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)
