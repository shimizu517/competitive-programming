def main():
    S = input()
    words = ["dream", "dreamer", "erase", "eraser"]
    dp = [False] * 100010
    dp[0] = True
    for idx in range(len(S)):  # 1
        if not dp[idx]:  # 2
            continue
        for w in words:
            if S[idx : idx + len(w)] == w:
                dp[idx + len(w)] = True
    if dp[len(S)]:
        print("YES")
    else:
        print("NO")


main()

# 例
# S='dreamerasererase'の場合、idx==0のとき、S[idx:idx+len('dream')]==dreamなので、dp[idx+len('dream)]=dp[5]=Trueとなる。
# 同様にdreamer, erase, eraserでもS[idx:idx+len(word)]をすると、dp = [1,0,0,0,0,1,0,1,0,....,0](1=True,0=False)となる。
# 1のfor文で2のif文がTrueになるのは、dp[idx]==1のとき、つまり前回まででwordのいずれかを繋げていった末尾のidx+1となるとき。
# 最後にdp[len(S)+1]が1となるのは、wordsのいずれかを繋げてSの最後まで行けたとき。
# 参考：https://qiita.com/259_Momone/items/991d31ccc1f830a1d578
