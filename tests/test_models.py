import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
    # This assumes the Magazine constructor needs 3 arguments
        magazine = Magazine(1, "Tech Weekly", "Technology")  # Ensure 3 arguments are passed
        self.assertEqual(magazine.id, 1)
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
if __name__ == "__main__":
    unittest.main()
