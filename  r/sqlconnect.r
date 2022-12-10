library(RSQLite)
library(DBI)
library(dplyr)
connection <- dbConnect(
    drv=SQLite(),
    dbname="/workspaces/Ravi-kumar-svce/database/code.db"
)
dbListTables(connection)
dbListTables(connection,'student')

surveys<-tbl(connection,'student')

surveys_df<-collect(surveys)
surveys_df