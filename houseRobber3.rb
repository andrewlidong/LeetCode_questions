def rob(root)
  rob_helper(root).max
end

def rob_helper(root)
  return [0, 0] if root.nil?

  left_taken, left_not_taken = rob_helper(root.left)
  right_taken, right_not_taken = rob_helper(root.right)

  [root.val + left_not_taken + right_not_taken, [left_taken, left_not_taken].max + [right_taken, right_not_taken].max]
end
