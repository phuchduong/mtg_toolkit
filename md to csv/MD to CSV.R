library(stringr)

setwd("D:/repos/mtg_toolkit")

input_file <- "inventory.md"

file_connection <- file(description = input_file, open = "r")

lines <- readLines(file_connection)

file_end <- length(lines)

card_df <- data.frame(
    cname=character(),
    qty=integer(),
    stringsAsFactors = FALSE
)

junk <- c()

card_pattern <- ".{1,}\\s\\|\\s\\d"

for( i in 1:file_end ){
    # sift through each line.
    # if it's a card add it to the data frame.
    # if not a card, add to the junk list
    line <- lines[i]
    is_card <- str_detect(string = line, pattern = card_pattern)
    
    new_row <- nrow(card_df) + 1
    if (is_card) {
        card_list <- str_split(string = line, pattern = "\\s\\|\\s")[[1]]
        print(card_list)
        print(card_list[1])
        print(card_list[2])
        card_df[new_row, "cname"] <- card_list[1]
        card_df[new_row, "qty"] <- card_list[2]
    } else {
        junk <- c(junk, c=line)
    }
}

write.csv(x = junk, file = "md_to_csv junk.csv", row.names = FALSE)
write.csv(x = card_df, file = "card qty.csv", row.names = FALSE)
