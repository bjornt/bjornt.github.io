# Ruby 4.0 removed Object#tainted? (the taint system was deprecated in 2.7,
# removed in 3.2). Liquid 4.0.3 still calls it. Restore it as a no-op that
# always returns false, which matches the pre-removal behavior for all
# normal objects.
class Object
  def tainted?
    false
  end
end unless Object.method_defined?(:tainted?)
