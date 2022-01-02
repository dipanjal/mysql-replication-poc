package com.poc.proxysql.controller;

import com.poc.proxysql.models.UserCreateRequest;
import com.poc.proxysql.models.UserDTO;
import com.poc.proxysql.models.UserUpdateRequest;
import com.poc.proxysql.service.UserServiceImpl;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @author dipanjal
 * @since 0.0.1
 */

@RestController
@RequiredArgsConstructor
public class UserController {

    private final UserServiceImpl userService;

    @GetMapping("/users")
    public ResponseEntity<List<UserDTO>> fetchAllUsers(){
        return ResponseEntity.ok(userService.getAllUsers());
    }

    @GetMapping("/users/{id}")
    public ResponseEntity<UserDTO> fetchUserById(@PathVariable long id){
        return ResponseEntity.ok(userService.getUserById(id));
    }

    @PostMapping("/users")
    public ResponseEntity<UserDTO> createUser(@RequestParam UserCreateRequest request){
        return ResponseEntity.ok(userService.createUser(request));
    }

    @PutMapping("/users")
    public ResponseEntity<UserDTO> updateUser(@RequestParam UserUpdateRequest request){
        return ResponseEntity.ok(userService.updateUser(request));
    }

    @DeleteMapping("/users/{id}")
    public ResponseEntity<UserDTO> deleteUser(@PathVariable long id){
        return ResponseEntity.ok(userService.deleteUser(id));
    }
}
