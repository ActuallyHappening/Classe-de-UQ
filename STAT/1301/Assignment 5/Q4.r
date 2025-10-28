library(lattice)
ebike_data = read.csv("EbikeEnergy.csv")
xyplot(Energy_Wh_per_km ~ Rider_Cargo_Mass_kg, data = ebike_data, xlab = "Rider + Cargo Mass (kg)", ylab = "Energy Use (Wh per km)")

model <- lm(Energy_Wh_per_km ~ Rider_Cargo_Mass_kg, data = ebike_data)
summary(model)
xyplot(residuals(model) ~ Rider_Cargo_Mass_kg, data = ebike_data)
qqnorm(residuals(model))
qqline(residuals(model))
