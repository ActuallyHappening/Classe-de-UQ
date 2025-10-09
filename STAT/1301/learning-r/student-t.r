curve(dt(x, df=1), ylim=c(0, 0.4), xlim = c(-5, 5), col = 1, ylab = "Density")
curve(dt(x, df=100), col=2, add=TRUE)
curve(dnorm(x), col=3, add=TRUE)
legend(2.1, 0.35, lty = 1, bty="n", legend = c("df=1, df=100", "norm"))
