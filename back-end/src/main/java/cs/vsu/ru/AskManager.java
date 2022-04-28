package cs.vsu.ru;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class AskManager {

    public static void main(String[] args) {
        SpringApplication.run(AskManager.class, args);
    }

    @GetMapping("/ask")
    public void ask() {
        //TODO: load file to server
    }

}
