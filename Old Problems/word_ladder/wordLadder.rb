# @param {String} begin_word
# @param {String} end_word
# @param {String[]} word_list
# @return {Integer}
def ladder_length(begin_word, end_word, word_list)
    word_set = Set.new word_list
    return 0 unless word_set.member?(end_word)
    queue = [[begin_word, 1]]
    while !queue.empty? do
        s = queue[0][0]
        l = queue[0][1]
        return l if s == end_word
        queue.delete_at(0)
        s.size.times do |i|
            t0 = s[0...i]
            t2 = s[(i + 1)...s.size]
            for c in "a".ord.."z".ord do
                next if c == s[i].ord
                t = t0 + c.chr + t2
                if word_set.member?(t) then
                    word_set.delete(t)
                    queue << [t, l + 1]
                end
            end
        end
    end
    0
end
