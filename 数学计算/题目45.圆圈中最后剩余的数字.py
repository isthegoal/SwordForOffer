# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
     典型的约瑟夫问题...........

     题目：0到n-1排成一圈，从0开始每次数m个数删除，求最后剩余的数  （不断数到当前开始的第m个，删去后继续
     继续进行循环，直到获得最后剩余的数字）

     分析：其实感觉方法是比较简单的，首先这里是 有m和n两个已知数。那我们需要 列举出可能出现的情况。
     【1】数学归纳法，动态规划规律法。从中可以找到合适的关系表达式【这里核心是公式的推导变换x'=(x+k)%n  但是我不知道怎么推出来的,好吧
     很多人都不知道怎么推导出来】。
            f[1]=0;
            f[i]=(f[i-1]+m)%i; (i>1)

      这里f[i]表示i个人玩游戏报m退出最后胜利者的编号，最后的结果自然是f[n]

     【2】使用约瑟夫环的思路进行求解。   就是每次更新循环长度  和位置索引，非常适合自己的思路。

        但是这里实现约瑟夫环，还有两种方式：
           （1）一种方法是使用  数组进行  环的维护，利用pop进行成员的弹出
           （2）第二种方式是使用 链表的方式。
        上面的两种方式中，数组方法虽然操作比较简单，但是因为数组的性质会导致其进行pop操作时，时间复杂度比较高。
        而链表的方式进行删除等操作时候的时间复杂度是O(1)的，而其空间复杂相对于数组只是多使用了一点，所以链表相对更好些。

'''

#m表示 报数时的间隔数，   n表示总数量。
def last_num(m,n):
    #边界条件
    if n<1 and m<1:
        return -1

    # last表示 现有递推的次数，我们根据  推导可以得到后面的过程，
    last=0
    # 如下是主要的推导【555...怎么推导的，我可不知道】，可以通过f(i-1)表示i-1个人玩游戏m退出游戏的编号，获得f(i)对应的编号。
    for i in range(2,n+1):
        last=(last+m)%i

    return last


#第二种 使用 约瑟夫环，而不是 数学归纳法的方式。   使用环，这种常规思路更适合自己，这里使用数组进行的保存。
def last_remain(m,n):
    #边界条件
    if n<1:
        return -1

    #创建初始数组
    con=range(n)

    final=-1
    start=0

    #使用while控制，每次弹出一个，当数组不为空，就可以一直进行 题意所示的环过程
    #题意过程： 先按照上次为m的位置开始，(start+m-1)%n找到新的位置，寻求进行更新。
    while con:
        #找到正确的当前环，要弹出的位置
        k=(start+m-1)%n

        final=con.pop(k)#注意这里索引和 数值的区分，我们最后获取得到具体数值即可

        #更新新的起点和   现在循环最大长度。
        n -= 1
        start=k

    return final






