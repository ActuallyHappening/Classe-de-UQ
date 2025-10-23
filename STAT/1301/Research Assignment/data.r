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

stripplot(Percentage~Cups, pch=music_choices, cex=1.5, data=data, xlab="Cups", main="Plot of percentage recall versus cups")
# stripplot(Percentage~Music, pch=cups_choices, cex=1.5, data=data, xlab="Music")

Music = data$Music
interaction.plot(data$Cups, Music, data$Percentage, xlab="Cups", ylab="Mean Percentage", main="Interactions",)
# interaction.plot(data$Music, data$Cups, data$Percentage) # converse

# With interaction factor
data.lm_int = lm(Percentage ~ Music * Cups, data=data)
anova(data.lm_int)
plot(data.lm_int)


# Without interaction factor
# anova(lm(Percentage ~ Music + Cups, data=data))

pairwise.t.test(data$Percentage, data$Music, p.adjust.method = "bonferroni")
pairwise.t.test(data$Percentage, data$Cups, p.adjust.method = "bonferroni")


#** Testing most extreme cases **
null = data[data$Music == "Silent" & data$Cups == "None",]
extreme = data[data$Music == "Classical" & data$Cups == "Many",]
t.test(null$Percentage, extreme$Percentage)
pairwise.t.test(null$Percentage, extreme$Percentage, p.adjust.method = "bonferroni")

silent = data[data$Music == "Silent",]
classical = data[data$Music == "Classical",]
t.test(silent$Percentage, classical$Percentage) # not significant

none = data[data$Cups == "None",]
many = data[data$Cups == "Many",]
t.test(none$Percentage, many$Percentage)

# Only for silent
anova(lm(Percentage~Cups, data=silent))
# Only for classical
anova(lm(Percentage~Cups, data=classical))
