# @param {String} s
# @param {String[]} word_dict
# @return {Boolean}
def word_break(s, dict)
    max = 0
    dic = Set.new dict
    dic.each do |v|
        max = [max, v.size].max
    end
    nextCheck = Set.new([0])

    while nextCheck.any?
        i = nextCheck.first
        nextCheck.delete i
        j = i
        while j <= s.size and j < i + 1 + max
            if dic.include?(s[i..j])
                nextCheck << j + 1
                return true if j == s.size
            end
            j += 1
        end
    end
    return false
end
