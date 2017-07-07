# install.packages("rvest")
library(rvest)
library(stringr)

#################################################################################
# get tcgplayer prices
#################################################################################
# scrape date, now
now <- Sys.time()

# url to scrape, then download page
url <- "http://magic.tcgplayer.com/db/search_result.asp?Set_Name=Battle%20for%20Zendikar"
webpage <- read_html(url)

html_tables <- webpage %>% html_nodes("table")

card_htable <- html_tables[9]

card_table <- as.data.frame(html_table(x = card_htable, fill = TRUE))

names(card_table) <- c("tcg_card", "tcg_mana_cost", "tcg_set_name", "tcg_rarity", "tcg_h", "tcg_m", "tcg_l")

card_table$tcg_date <- now

tcg <- card_table[,c("tcg_card", "tcg_set_name", "tcg_h", "tcg_m", "tcg_l", "tcg_date")]

#################################################################################
# read in inventory
#################################################################################
setwd("D:/repos/mtg_toolkit")
inv <- read.csv(file = "inventory.csv", header = TRUE, stringsAsFactors = FALSE)
names(inv)[1] <- c("inv_card")

#################################################################################
# create universal card name list
#################################################################################

# makes a universal card name list
card_name <- c(inv$card_name, price_table$card_name)

# trim white space, lower case, remove duplicates, sort alpha
card_name <- trimws(card_name)
card_name <- tolower(card_name)
card_name <- unique(card_name)
card_name <- sort(card_name)

#################################################################################
# merge and cross reference
#################################################################################
master <- as.data.frame(card_name, stringsAsFactors = FALSE)

# full outer join of card names and tcgplayer pricing table
inv$key <- inv$inv_card
inv$key <- trimws(inv$key)
inv$key <- tolower(inv$key)
master <- merge(x=master, y=inv, by.x="card_name", by.y="key", all = TRUE)
master <- master[,c("card_name", "qty", "is_bulk")]

# full outer join of 
tcg$key <- tcg$tcg_card
tcg$key <- trimws(tcg$key)
tcg$key <- tolower(tcg$key)
tcg <- tcg[,c("key", "tcg_set_name", "tcg_h", "tcg_m", "tcg_l", "tcg_date")]
master <- merge(x=master, y=tcg, by.x="card_name", by.y="key", all = TRUE)

master$qty <- as.numeric(master$qty)

#################################################################################
# egress
#################################################################################

# write file out as a csv
o.filename <- paste("inventory ", as.character(now), ".csv", sep = "")
o.filename <- str_replace_all(string = o.filename, pattern = ":", replacement = ".")
o.filename <- str_replace_all(string = o.filename, pattern = " ", replacement = "_")
write.csv(
    x = master,
    file = o.filename,
    row.names = FALSE,
    na=""
)

