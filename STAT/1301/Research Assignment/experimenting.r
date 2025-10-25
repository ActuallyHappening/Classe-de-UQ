# Create example data
set.seed(123)
group1 <- rnorm(100, mean = 5, sd = 1.5)
group2 <- rnorm(100, mean = 6, sd = 1.2)
group3 <- rnorm(100, mean = 5.5, sd = 1.8)

# Method 1: Using base R with custom positioning and transparency
# par(mar = c(5, 4, 4, 2))
boxplot(group1, at = 1, xlim = c(0.5, 1.5), ylim = c(0, 10),
        col = rgb(1, 0, 0, 0.5), border = "darkred",
        boxwex = 0.3, main = "Overlapping Boxplots",
        xlab = "Category", ylab = "Value", xaxt = "n")

boxplot(group2, at = 1.15, add = TRUE,
        col = rgb(0, 0, 1, 0.5), border = "darkblue",
        boxwex = 0.3)

boxplot(group3, at = 1.3, add = TRUE,
        col = rgb(0, 1, 0, 0.5), border = "darkgreen",
        boxwex = 0.3)

axis(1, at = 1.15, labels = "All Groups")
legend("topright", legend = c("Group 1", "Group 2", "Group 3"),
       fill = c(rgb(1, 0, 0, 0.5), rgb(0, 0, 1, 0.5), rgb(0, 1, 0, 0.5)),
       border = c("darkred", "darkblue", "darkgreen"))
