def statistics(grades):
	mean=numpy.mean(grades)
	std=numpy.std(grades)
	high_score=max(grades)
	low_score=min(grades)
	return mean,std,high_score,low_score
