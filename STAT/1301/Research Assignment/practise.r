x = data.frame(Placebo=c(5,8,7,7,10,8),T2=c(4,6,6,3,5,6),
T3=c(6,4,4,5,4,3),T4=c(7,4,6,6,3,5),T5=c(9,3,5,7,7,6))
coldsore = stack(x)
names(coldsore) = c("times", "treatment")

tapply(coldsore$times, coldsore$treatment, summary)

library(lattice)
boxplot(times~treatment, data=coldsore, xlab="Treatment")

coldsore.lm = lm(times~treatment, data=coldsore)
coldsore.lm
anova(coldsore.lm)
