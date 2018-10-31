def trap(height)
    return 0 if height.length == 0

#     make head and tail of height peaks
    pre_process!(height)

#     find max element's index
    max_ele, max_idx = -1, -1

    height.each_with_index do |ele, idx|
        next if max_ele >= ele

        max_ele = ele
        max_idx = idx
    end

    calc_trap(height[0..max_idx]) + calc_trap(height[max_idx..-1].reverse)
end

def calc_trap(height)
    return 0 if height.length <3
    n = height.length
    pos = 0
    res = 0
    peak = height[0]

    loop do
        p1 = pos
        pos += 1 while pos + 1 < n && height[pos] >= height[pos + 1]
        pos += 1 while pos + 1 < n && height[pos] <= height[pos + 1]
        p2 = pos

        height [p1+1..p2].each do |ele|
            next if peak <= ele
            res += (peak - ele)
        end

        peak = height[pos] if peak < height[pos]

        break if pos + 1 == n
    end

    res
end

    def pre_process!(height)
        n = height.length

#         shift until first peak
        i = 0
        i += 1 while i + 1 < n && height[i] <= height[i + 1]

#          pop until last peak
        j = n - 1
        j -= 1 while j - 1 >= 0 && height[j] <= height[j - 1]

        return 0 if i >= j

        height[i..j]
        end
