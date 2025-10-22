data = read.csv("Data.csv")
data$Music = factor(data$Music, levels = c("Silent", "Classical"))
data$Cups = factor(data$Cups, levels = c("None", "Medium", "Many"))

library(lattice)

# cex:
# ‘cex’ A numeric multiplier to control character sizes for
# axis labels.  Can be a vector of length 2

# 4 = cross, 1 = circle
# cross = silent, cirlce = classical
chs = c(rep(4,18),rep(1,18)) # define two groups of plotting characters

stripplot(Percentage~Cups, pch=chs, cex=1.5, data=data, xlab="Cups")



6 chs = c(rep(4,9),rep(1,9)) # define two groups of plotting characters
7 stripplot(Yield∼Fertilizer,pch=chs,cex=1.5,data=crop,xlab="Fertilizer")
8 #stripplot(Yield∼Fertilizer,groups=Pesticide,cex=1.5,data=crop,
9 # xlab="Fertilizer")
