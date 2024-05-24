
#https://leetcode.com/problems/valid-parentheses/description/
#1回目　22分ほどで思いついた結果をかけて:のつけ忘れやインデントなどの細かい文法ミスを除けばあっているコードではあった
#今日はここまで
#Two Sumについてのコメントいただく前に書いたので余計なbreakがあります

class Solution:
    def isValid(self, s: str) -> bool:
        #for i in range(0,len(s)):
        #flag = False
        def ParL(parS,parE):
            parSL = [i for i, x in enumerate(list(s)) if x == parS] #良く使うのに使おうとする度に調べてる気がする
            parEL = [i for i, x in enumerate(list(s)) if x == parE]
            if len(parSL) != len(parEL):
                return False
            else:
                for i in range(0,len(parSL)):
                    if parSL[i] > parEL[i]:
                        return False
                        break
                    else:
                        continue
                        if i == (len(parSL)-1):
                            return True 

        if ParL("(",")") or ParL("{","}") or ParL("[","]")  == False:
            return False
        else:
            return True
    
    #答えを送信して、正解になったら、まずは一段階目です。次にコードを読みやすくするようにできるだけ整えましょう。
    #return

class Solution:
    def isValid(self, s: str) -> bool:
        #for i in range(0,len(s)):
        #flag = False
        def ParL(parS,parE):
            parSL = [i for i, x in enumerate(list(s)) if x == parS]
            parEL = [i for i, x in enumerate(list(s)) if x == parE]
            if len(parSL) != len(parEL):
                return False
            else:
                for i in range(0,len(parSL)):
                    if parSL[i] > parEL[i]:
                        return False
                    else:
                        continue
                        if i == (len(parSL)-1):
                            return True 

        if ParL("(",")") or ParL("{","}") or ParL("[","]")  == False:
            return False
        else:
            return True




    #これで動くコードになったら二段階目です。そしたららまた全部消しましょう。今度は、時間を測りながら、もう一回、書きましょう。
    #書いてアクセプトされたら文字消してもう一回書きましょう。
    #これを10分以内に一回もエラーを出さずに書ける状態になるまで続けてください。3回続けてそれができたらその問題はひとまず丸です。
    
    #数日経ってやろうとしたところ、突然上のコードを書いた時の冴えが消えており
    #数日前の自分は天才だったのかもしれないと思うに至りました。

    #leetcodeのそもそもの使い方を分かっておらず、submitしたら全然通らないコードだった。
    #Step1として書いたコードがこちら。
    #"([)]"のtest caseの答えはfalseだと言われるがなぜfalseなのか分からない……。

    class Solution:
    def isValid(self, s: str) -> bool:
        def ParL(parS, parE):
            parSL = [i for i, x in enumerate(list(s)) if x == parS]
            parEL = [i for i, x in enumerate(list(s)) if x == parE]
            print(parSL,parEL)
            if parSL == [] and parEL == []:
                #print(parS,parE,"True")
                return True
            if len(parSL) != len(parEL):
                #print(parS,parE,"False")
                return False
            else:
                for i in range(0, len(parSL)):
                    if parSL[i] > parEL[i]:
                        #print(parS,parE,"False")
                        return False
                    else:
                        if i == (len(parSL)-1):
                            #print(parS,parE,"True")
                            return True
        print(ParL("(",")"), ParL("{","}"), ParL("[","]"))
        return all([ParL("(",")") , ParL("{","}") , ParL("[","]")])
       
    #答えを見た stackを使います
    #自分で考えてここまで解いたんですが1test caseだけ通らない……今日はここまでとします。

    class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for txt in s:
            if txt == '}' or txt == ')' or txt == ']':
                if not stack:
                    return False
            if txt == '}':
                if "{" == stack[-1]:
                        stack.pop()
            if txt == ')':
                if "(" == stack[-1]:
                        stack.pop()
            if txt == ']':
                if "[" == stack[-1]:
                        stack.pop()
                else:
                    return False
            if txt == '{' or txt == '(' or txt == '[':
                stack.append(txt)
        if stack == []:
            return True
            