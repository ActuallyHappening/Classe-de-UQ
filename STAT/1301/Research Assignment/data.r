data = read.csv("Data.csv")
data$Music = factor(data$Music, levels = c("Silent", "Classical"))
data$Cups = factor(data$Cups, levels = c("None", "Medium", "Many"))

# data2 = read.csv("Data excluding low.csv")
# data2$Music = factor(data2$Music, levels = c("Silent", "Classical"))
# data2$Cups = factor(data2$Cups, levels = c("None", "Medium", "Many"))

library(lattice)

# 4 = cross, 1 = circle, 3 = plus
# cross = silent, cirlce = classical
music_choices = c(rep(4,18),rep(1,18)) # define two groups of plotting characters
# cross = none, plus = medium, circle = many
#cups_choices = c(rep(c(rep(4, 6), rep(3, 6), rep(1, 6)), 2))

stripplot(Percentage~Cups, pch=music_choices, cex=1.5, data=data, xlab="Cups", main="Plot of percentage recall versus cups")
# stripplot(Percentage~Music, pch=cups_choices, cex=1.5, data=data, xlab="Music")

Music = data$Music
interaction.plot(data$Cups, Music, data$Percentage, xlab="Cups", ylab="Mean Percentage", main="Interactions",)
# interaction.plot(data$Music, data$Cups, data$Percentage) # converse

# With interaction factor
data.lm_int = lm(Percentage ~ Music * Cups, data=data)
anova(data.lm_int)
# plot(data.lm_int)


# Without interaction factor
# anova(lm(Percentage ~ Music + Cups, data=data))

pairwise.t.test(data$Percentage, data$Music, p.adjust.method = "bonferroni")
pairwise.t.test(data$Percentage, data$Cups, p.adjust.method = "bonferroni")


#** Testing most extreme cases **
# null = data[data$Music == "Silent" & data$Cups == "None",]
# extreme = data[data$Music == "Classical" & data$Cups == "Many",]
# t.test(null$Percentage, extreme$Percentage)
# pairwise.t.test(null$Percentage, extreme$Percentage, p.adjust.method = "bonferroni")

silent = data[data$Music == "Silent",]
classical = data[data$Music == "Classical",]
# t.test(silent$Percentage, classical$Percentage) # not significant

none = data[data$Cups == "None",]
many = data[data$Cups == "Many",]
# t.test(none$Percentage, many$Percentage)

# Only for silent
data.lm_silent = lm(Percentage~Cups, data=silent)
anova(data.lm_silent)
# plot(data.lm_silent)

# # Only for classical
# anova(lm(Percentage~Cups, data=classical))

boxplot(data$Percentage, ylim=c(66, 100), ylab="Percentage recall", main="Percentage recall over all samples")

silent_many = data[data$Music == "Silent" & data$Cups == "Many",]
summary(silent_many)
sd(silent_many$Percentage)
classical_many = data[data$Music == "Classical" & data$Cups == "Many",]
summary(classical_many)
sd(classical_many$Percentage)

boxplot(silent_many$Percentage, ylim=c(66, 100), ylab="Percentage recall", main="Percentage recall for Music = Silent and Cups = 6 (j=3)")
boxplot(classical_many$Percentage, ylim=c(66, 100), ylab="Percentage recall", main="Percentage recall for Music = Classical and Cups = 6 (j=3)")

# **Experimenting**

# Create a combined factor for all subregions
data$Subregion <- interaction(data$Music, data$Cups, sep = " & ")

# Create boxplot
boxplot(Percentage ~ Subregion, data = data,
        main = "Percentage by Music and Cups",
        ylab = "Percentage",
        xlab = "Music & Cups",
        las = 2, names = c("S-None", "S-Med", "S-High",
                          "C-None", "C-Med", "C-High"))

# install.packages("tidyverse")
library(ggplot2)

ggplot(data, aes(x = interaction(Music, Cups), y = Percentage, fill = Music)) +
  geom_boxplot() +
  labs(title = "Percentage by Music and Cups",
       x = "Condition",
       y = "Percentage") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
