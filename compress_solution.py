
class CompressString():
	def compress(self, string):
		if string is None or not string:
			return string
		result = ''
		print(string)
		prev_char = string[0]
		count = 0
		for char in string:
			if char == prev_char:
				count += 1
			else:
				result += self._calc_partial_result(prev_char, count)
				prev_char = char
				count = 1
		result += self._calc_partial_result(prev_char, count)
		return result
	def _calc_partial_result(self, prev_char, count):
		return prev_char + (str(count) if count > 1 else '')
	
	
def main():
	test = CompressString()
	compressed_String = test.compress("AAABCCDD")
	print(compressed_String)
	
	
if __name__ == "__main__":
	main()