class LRUCache

=begin
    :type capacity: Integer
=end
    def initialize(capacity)
        @capacity = capacity
        @cache = {}
    end


=begin
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
        return -1 unless @cache[key]
        value = @cache.delete(key)
        @cache[key] = value
        value
    end


=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
        @cache.delete(key)
        if @cache.length >= @capacity
            @cache.shift
            @cache[key] = value
            value
        else
            @cache[key] = value
        end
    end
end

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
