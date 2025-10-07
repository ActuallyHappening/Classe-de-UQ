heart = read.csv("heart.csv", colClasses = c(
	'numeric', 'factor', 'numeric', 'factor', 'numeric', 'factor', 'numeric', 'numeric', 'numeric', 'factor', 'factor', 'numeric', 'factor'
))

plot(heart$serum_sodium, heart$ejection_fraction)
log10cp = log10(heart$cp)
log10sc = log10(heart$serum_creatinine)

qvars = cbind(heart$age, log10cp, heart$ejection_fraction, heart$platelets, log10sc, heart$serum_sodium)
dimnames(qvars)[[2]] = c("age", "log10cp", "ejection_fraction", "platlets", "log10sc", "serum_sodium")

pairs(qvars)
