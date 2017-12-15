library(ggplot2)
library(ggalt)
library(scales)
library(dplyr)
theme_set(theme_classic())

avg_mkt_cap <- mean(crypto$market_cap_usd)
crypto <- read.csv("~/Downloads/crypto.csv")
crypto$percent_change_24h<-crypto$percent_change_24h/100
crypto$percent_change_1h<-crypto$percent_change_1h/100
crypto<-filter(crypto, rank <= 25)
crypto <- crypto[order(crypto$percent_change_24h,decreasing = TRUE),]
crypto$name <- factor(crypto$name, levels=as.character(crypto$name))  # for right ordering of the dumbells
updated<-unique(as.Date(crypto$last_updated))

gg <- ggplot(crypto, aes(x=percent_change_1h, xend=percent_change_24h, y=name, group=name)) + 
  geom_dumbbell(color="#72726d",
                colour_x ="#070707", 
                size=1,
                size_x = 2,
                size_xend = 2,
                colour_xend="#edd81a",  
                show.legend = TRUE) + 
  scale_x_continuous(label=percent) + 
  labs(x=NULL, 
       y=NULL, 
       title=paste("Top 25 Crypto by Marketcap as of",updated), 
       subtitle="1hr v. 24hr performance", 
       caption="Source: BlockhouseAU, CoinMarketCap") +
  theme(plot.title = element_text(hjust=0.5, face="bold"),
        plot.background=element_rect(fill="#f7f7f7"),
        panel.background=element_rect(fill="#f7f7f7"),
        panel.grid.minor=element_blank(),
        panel.grid.major.y=element_blank(),
        panel.grid.major.x=element_line(),
        axis.ticks=element_blank(),
        legend.position="top",
        panel.border=element_blank())
plot(gg)
