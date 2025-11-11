from bs4 import BeautifulSoup
import csv


# Load webpage into file for beautiful soup to parse
local_file = "full_exhibitor_site.html"
page = open(local_file, encoding="utf-8")

soup = BeautifulSoup(page.read(), "html.parser")

# Take just the full exhibitor table and not featured
soup_table = soup.findAll("table", {"class": "results-table word-wrap"})[1]
exhibitor_list = soup_table.find_all("a")

out_list = []
for entry in exhibitor_list:
    out_list.append(entry.get_text(strip=True))

# Filter out empty/None entries
filtered_list = list(filter(None, out_list))

bad_str = "\n                                      "
exhibitors = [str(x).replace(bad_str, " ") for ind, x in enumerate(filtered_list) if ind % 2 == 0]
booth_num = [x for ind, x in enumerate(filtered_list) if ind % 2 == 1]

print(exhibitors)
print(f"Number of companies: {len(exhibitors)}")

# with open("output.csv", "w", newline="") as csv_out:
#     outfile = csv.writer(csv_out)

#     # Columns
#     outfile.writerow(["Exhibitor", "Booth"])

#     for i in range(0, len(exhibitors))


    