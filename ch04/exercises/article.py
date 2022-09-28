article = "At approximately 2:10 PM local time, U.S. forces brought down an Iranian Mojer-6 Unmanned Aerial Vehicle headed in the direction of Erbil as it appeared as a threat to USCENTCOM forces in the area, US Central Command, which oversees the US military presence in the Middle East, said in a statement.Earlier Wednesday, nine people were killed, including civilians, after Iran’s Islamic Revolutionary Guard Corps targeted Kurdish separatist groups in northern Iraq, Kurdistan Regional Government [KRG] Health Minister Saman Barzanji told CNN."
subsitutions = {
  "forces":"little gun guys",
  "Iran":"Over yander", 
  "killed":"hugged",
  "Vehicle":"unarmed family",
  "military":"homies"
}

for i, value in subsitutions.items():
  article = article.replace(i,value)

print(article)