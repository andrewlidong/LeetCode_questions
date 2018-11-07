def find_ladders(begin_word, end_word, word_list)
  return [] unless (unvisited = word_list.to_set).include?(end_word)
  words_by_transform = graph_word_transforms(begin_word, end_word, unvisited)
  reverse_dfs_paths(begin_word, end_word, words_by_transform)
end

def graph_word_transforms(begin_word, end_word, unvisited)
  words_by_transform = Hash.new { |h, k| h[k] = Set.new }
  transformations = Array(0...begin_word.size).product(Array('a'..'z'))

  unvisited.delete(end_word)
  begin_layer, end_layer = Set.new, Set[end_word]
  prev_layer, curr_layer, next_layer = end_layer, begin_layer, Set[begin_word]

  until next_layer.empty? || end_layer.any? { |t| words_by_transform[t].intersect?(begin_layer) }
    curr_layer.replace(next_layer)
    curr_layer, prev_layer = prev_layer, curr_layer
    unvisited.subtract(prev_layer)
    next_layer.clear

    curr_layer.each do |word|
      transformations.each do |i, c|
        next if word[i] == c

        transform = word.dup.tap { |w| w[i] = c }
        next_layer << transform if (is_neighbor = unvisited.include?(transform))
        if is_neighbor || prev_layer.include?(transform)
          orig_word, variant = curr_layer.equal?(begin_layer) ? [word, transform] : [transform, word]
          words_by_transform[variant] << orig_word
        end

      end
    end
  end
  words_by_transform
end

def reverse_dfs_paths(begin_word, end_word, word_graph)
  paths, path = [], []
  stack = [[end_word, 1]]
  until stack.empty?
    word, lvl = stack.pop
    path.pop until path.size < lvl
    path << word

    if word == begin_word
      paths << path.reverse
    else
      word_graph[word].each { |w| stack << [w, lvl + 1] }
    end
  end
  paths
end
