'''
     题目：翻转一个英文句子中的单词顺序，标点和普通字符一样处理

     分析：这里目标非常简单  ，就是一个全  翻转，  这个很容易的 让我想到了 ::-1的操作。

     这里要注意，在python中 字符串是不可变对象，所以需要先转化为列表然后转回去。
'''

def rotate_string(sentence):
    #首先完全的切分
    tmp=sentence.split()
    #这种获取  逆序序列 并进行组合成字符串的操作吧
    return ' '.join(tmp[::-1])




'''
     题目：把字符串的前面的若干位移到字符串的后面

     分析：这里的话，设定函数的话，就是    字符串和  前方多少位置移动到后面。
                一种简单的思路，前向  pop，外加后向append 吗 ？
                另一个简单的思路，使用s[n:] + s[:n]  ，这个简直不要太简单
'''
def rotate_s(s,n):
    if not s:
        return ''
    #一个重要的  ，万一   n比s 还长的话，  算了，这个情况暂不做考虑。
    n%=len(s)
    return s[n:]+s[:n]