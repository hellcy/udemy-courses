package com.example.demo.bootstrap;

import com.example.demo.model.Author;
import com.example.demo.model.Book;
import com.example.demo.repositories.AuthorRepository;
import com.example.demo.repositories.BookRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class BootStrapData implements CommandLineRunner {
  private final AuthorRepository authorRepository;
  private final BookRepository bookRepository;

  public BootStrapData(AuthorRepository authorRepository, BookRepository bookRepository) {
    this.authorRepository = authorRepository;
    this.bookRepository = bookRepository;
  }


  @Override
  public void run(String... args) throws Exception {
    Author yuan = new Author("Yuan", "Cheng");
    Book book1 = new Book("Book1 Name", "1");

    yuan.getBooks().add(book1);
    book1.getAuthors().add(yuan);

    authorRepository.save(yuan);
    bookRepository.save(book1);

    Author nancy = new Author("Nancy", "Yang");
    Book book2 = new Book("Book2 Name", "2");

    nancy.getBooks().add(book2);
    book2.getAuthors().add(nancy);

    authorRepository.save(nancy);
    bookRepository.save(book2);

    System.out.println("Started in Bootstrap");
    System.out.println("Number of book2: " + bookRepository.count());
  }
}
