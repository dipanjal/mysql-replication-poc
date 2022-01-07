package com.poc.proxysql.contrioller;


import com.poc.proxysql.models.UserCreateRequest;
import com.poc.proxysql.models.UserDTO;
import com.poc.proxysql.models.UserUpdateRequest;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.web.server.LocalServerPort;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.core.env.Environment;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import java.util.List;

@Slf4j
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class UserControllerTests {

    @Autowired
    private TestRestTemplate restTemplate;

    @Autowired
    private Environment env;

    @LocalServerPort
    private int port;


    private String getBaseUrl() {
        return "http://localhost:"+port;
    }


    @Test
    @Disabled
    public void testFetchAllUsers() throws InterruptedException {
        int limit = env.getProperty("application-test.testFetchAllUsers.repeat", Integer.TYPE, 1);
        long interval =  env.getProperty("application-test.testFetchAllUsers.delay", Long.TYPE, 2000L);

        ParameterizedTypeReference<List<UserDTO>> typeReference = new ParameterizedTypeReference<>() {};

        for(int i = 0; i < limit; i++) {
            log.info("[{}] -> {}", i+1, getBaseUrl()+"/users");
            ResponseEntity<List<UserDTO>> response = restTemplate.exchange(getBaseUrl()+"/users", HttpMethod.POST, null, typeReference);
            Assertions.assertEquals(response.getStatusCode(), HttpStatus.OK);
            Thread.sleep(interval);
        }
    }


    @Test
    @Disabled
    public void createNewUserTest() {
        ParameterizedTypeReference<UserDTO> typeReference = new ParameterizedTypeReference<>() {};
        UserCreateRequest request = new UserCreateRequest("Jhon Doe");
        ResponseEntity<UserDTO> response = restTemplate
                .exchange(
                        getBaseUrl()+"/users",
                        HttpMethod.POST,
                        new HttpEntity<>(request),
                        typeReference
                );
        Assertions.assertEquals(response.getStatusCode(), HttpStatus.OK);
    }

    @Test
    @Disabled
    public void updateUserTest() {
        ParameterizedTypeReference<UserDTO> typeReference = new ParameterizedTypeReference<>() {};
        UserUpdateRequest request = new UserUpdateRequest(1, "Dipanjal");
        ResponseEntity<UserDTO> response = restTemplate
                .exchange(
                        getBaseUrl()+"/users",
                        HttpMethod.PUT,
                        new HttpEntity<>(request),
                        typeReference
                );
        Assertions.assertEquals(response.getStatusCode(), HttpStatus.OK);
    }
}
