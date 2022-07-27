def solution(s, n):
    answer = ''
    big = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    for i in range(len(s)):
        if(s[i] in big):
            index = big.index(str(s[i]))
            if(index + n) >= 26:
                answer += str(big[index + n - 26])
            else:
                answer += str(big[index + n])
        elif(s[i] in small):
            index = small.index(str(s[i]))
            if(index + n) >= 26:
                answer += str(small[index + n - 26])
            else:
                answer += str(small[index + n])
        else:
            answer += " "
    return answer