package com.example.demo.bootstrap;

import com.example.demo.model.Author;
import com.example.demo.model.Book;
import com.example.demo.model.Publisher;
import com.example.demo.repositories.AuthorRepository;
import com.example.demo.repositories.BookRepository;
import com.example.demo.repositories.PublisherRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class BootStrapData implements CommandLineRunner {
  private final AuthorRepository authorRepository;
  private final BookRepository bookRepository;
  private final PublisherRepository publisherRepository;

  public BootStrapData(AuthorRepository authorRepository, BookRepository bookRepository, PublisherRepository publisherRepository) {
    this.authorRepository = authorRepository;
    this.bookRepository = bookRepository;
    this.publisherRepository = publisherRepository;
  }


  @Override
  public void run(String... args) throws Exception {
    Author yuan = new Author("Yuan", "Cheng");
    Book book1 = new Book("Book1 Name", "1");
    Publisher publisher1 = new Publisher("Waterloo", "Sydney", "NSW", "2017");

    yuan.getBooks().add(book1);
    book1.getAuthors().add(yuan);

    authorRepository.save(yuan);
    bookRepository.save(book1);
    publisherRepository.save(publisher1);

    Author nancy = new Author("Nancy", "Yang");
    Book book2 = new Book("Book2 Name", "2");
    Publisher publisher2 = new Publisher("Lardelli", "Ryde", "NSW", "2042");

    nancy.getBooks().add(book2);
    book2.getAuthors().add(nancy);

    authorRepository.save(nancy);
    bookRepository.save(book2);
    publisherRepository.save(publisher2);

    System.out.println("Started in Bootstrap");
    System.out.println("Number of books: " + bookRepository.count());
    System.out.println("Number of publishers: " + publisherRepository.count());
  }
}
