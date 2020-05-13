package golangleetcode

func isValidSudoku(board [][]byte) bool {

	// row validate
	for i := 0; i < 9; i++ {
		filled := make(map[byte]int, 9)
		for j := 0; j < 9; j++ {
			if board[i][j] == 46 {
				continue
			}
			if _, ok := filled[board[i][j]]; ok {
				return false
			}
			filled[board[i][j]] = 1
		}
	}
	// column validate
	for i := 0; i < 9; i++ {
		filled := make(map[byte]int, 9)
		for j := 0; j < 9; j++ {
			if board[j][i] == 46 {
				continue
			}
			if _, ok := filled[board[j][i]]; ok {
				return false
			}
			filled[board[j][i]] = 1
		}
	}
	// grid validate
	for x := 0; x < 9; x += 3 {
		for y := 0; y < 9; y += 3 {
			filled := make(map[byte]int, 9)
			for i := 0; i < 3; i++ {
				for j := 0; j < 3; j++ {
					if board[i+x][j+y] == 46 {
						continue
					}
					if _, ok := filled[board[i+x][j+y]]; ok {
						return false
					}
					filled[board[i+x][j+y]] = 1
				}
			}
		}
	}
	return true
}
