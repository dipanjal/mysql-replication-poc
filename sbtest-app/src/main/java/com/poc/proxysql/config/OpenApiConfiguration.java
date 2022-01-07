package com.poc.proxysql.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Contact;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.info.License;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @author dipanjal
 * @since 0.0.1
 */

@Configuration
public class OpenApiConfiguration {

    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(this.getApiInfo());
    }

    private Info getApiInfo() {
        return new Info()
                .title("User Management REST Api Service")
                .version("1.0")
                .description("Rest Api server for Mysql Replication Test")
                .contact(getContactInfo())
                .termsOfService("http://swagger.io/terms/")
                .license(new License().name("Apache 2.0").url("http://springdoc.org"));
    }

    private Contact getContactInfo() {
        return new Contact()
                .name("Dipanjal Maitra")
                .email("dipanjalmaitra@gmail.com")
                .url("https://github.com/dipanjal");
    }
}
