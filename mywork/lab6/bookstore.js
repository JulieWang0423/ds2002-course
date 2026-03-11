// Task 2: use database
//use bookstore;

// Task 3: insert first author
db.authors.insertOne({
    "name": "Jane Austen",
    "nationality": "British",
    "bio": {
      "short": "English novelist known for novels about the British landed gentry.",
      "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
    }
  })

// Task 4: update to add birthday
db.authors.updateOne({ "name": "Jane Austen" }, { "$set": { "birthday": "1775-12-16" } });

// Task 5: insert four more authors
db.authors.insertMany([
    {
      "name": "Ernest Hemingway",
      "nationality": "American",
      "bio": {
        "short": "American novelist and short-story writer.",
        "long": "Ernest Miller Hemingway was an American novelist, short-story writer, and journalist. His economical and understated style—which he termed the iceberg theory—had a strong influence on 20th-century fiction."
      },
      "birthday": "1899-07-21"
    },
    {
      "name": "Gabriel García Márquez",
      "nationality": "Colombian",
      "bio": {
        "short": "Master of magical realism.",
        "long": "Gabriel José de la Concordia García Márquez was a Colombian novelist, short-story writer, screenwriter, and journalist, known affectionately as Gabo throughout Latin America."
      },
      "birthday": "1927-03-06"
    },
    {
      "name": "Haruki Murakami",
      "nationality": "Japanese",
      "bio": {
        "short": "Contemporary Japanese writer of surrealist fiction.",
        "long": "Haruki Murakami is a Japanese writer. His books and stories have been bestsellers in Japan as well as internationally, with his work being translated into 50 languages."
      },
      "birthday": "1949-01-12"
    },
    {
      "name": "Virginia Woolf",
      "nationality": "British",
      "bio": {
        "short": "English writer and pioneer of modernism.",
        "long": "Adeline Virginia Woolf was an English writer, considered one of the most important modernist 20th-century authors and a pioneer in the use of stream of consciousness as a narrative device."
      },
      "birthday": "1882-01-25"
    }
  ])

// Task 6: total count
db.authors.countDocuments({});

// Task 7: British authors, sorted by name
db.authors.find({ "nationality": "British" }).sort({ "name": 1 });