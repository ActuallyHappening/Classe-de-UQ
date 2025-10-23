data = read.csv("Data.csv")
data$Music = factor(data$Music, levels = c("Silent", "Classical"))
data$Cups = factor(data$Cups, levels = c("None", "Medium", "Many"))

library(lattice)

# cex:
# ‘cex’ A numeric multiplier to control character sizes for
# axis labels.  Can be a vector of length 2

# 4 = cross, 1 = circle, 3 = plus
# cross = silent, cirlce = classical
music_choices = c(rep(4,18),rep(1,18)) # define two groups of plotting characters
# cross = none, plus = medium, circle = many
cups_choices = c(rep(c(rep(4, 6), rep(3, 6), rep(1, 6)), 2))

stripplot(Percentage~Cups, pch=music_choices, cex=1.5, data=data, xlab="Cups", main="Percentage ")
stripplot(Percentage~Music, pch=cups_choices, cex=1.5, data=data, xlab="Music")

stripplot(Percentage~Music*Cups, cex=1.5, data=data)

Music = data$Music
interaction.plot(data$Cups, Music, data$Percentage, xlab="Cups", ylab="Mean Percentage", main="Interactions",)
# interaction.plot(data$Music, data$Cups, data$Percentage) # converse

# 6 chs = c(rep(4,9),rep(1,9)) # define two groups of plotting characters
# 7 stripplot(Yield∼Fertilizer,pch=chs,cex=1.5,data=crop,xlab="Fertilizer")
# 8 #stripplot(Yield∼Fertilizer,groups=Pesticide,cex=1.5,data=crop,
# 9 # xlab="Fertilizer")
