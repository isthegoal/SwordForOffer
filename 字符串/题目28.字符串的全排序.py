# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：求输入字符串的全排列

      分析：这样的全排序，一个很明确的思想思想就是  对所有组合情况的遍历， 并且，  这里肯定要利用到递归。
              可以先训练确定第一位，然后对剩余位置，使用递归的方法不断循环往后确定，从而当字符串为空时，就是 较为完全的一个排序成的结果

      思路：需要两个容器吧， 一个存放 现有组合的字符，另一个是存放 现有拼好的字符串。

           注意在递归时候，记住对现有组合的字符  集合，在递归的最后一句进行pop还原操作，  这样才能完好的对后来的可能情况获取腾出位置。

           递归操作中的  最后的还原操作至关重要。
'''
def my_permutation(s):
    #创建存储两个   信息的容器     一个是现有字符，  一个是已经拼好的字符串
    str_set=[]
    ret=[]

    def permutation(string):
        #每个递归中非常重要的部分，对于所有可以的，都进行遍历下
        for i in string:
            #去除当前后剩余的 字符.   并将当前的放到  一个现有已知的集合中
            str_tem=string.replace(i,'')
            str_set.append(i)

            #重要的， 如果当前去除现在字符 后，  还有很多剩余字串时，则进行 递归的往后查找
            if len(str_tem>0):
                permutation(str_tem)
            else:
                #成功的，当当前字串序列都被用完时，认为是成功的一个字串
                ret.append(''.join(str_set))

            #非常重要的， 对已经看过的信息  在  递归的最后一步，进行信息空间的腾出位置
            str_set.pop()

    permutation(s)
    return ret

