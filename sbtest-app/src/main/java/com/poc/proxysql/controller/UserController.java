package com.poc.proxysql.controller;

import com.poc.proxysql.models.UserCreateRequest;
import com.poc.proxysql.models.UserDTO;
import com.poc.proxysql.models.UserUpdateRequest;
import com.poc.proxysql.service.UserServiceImpl;
import io.swagger.v3.oas.annotations.Operation;
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
    @Operation(description = "Read all Users")
    public ResponseEntity<List<UserDTO>> fetchAllUsers() {
        return ResponseEntity.ok(userService.getAllUsers());
    }

    @GetMapping("/users/{id}")
    @Operation(description = "Read Specific User by Id")
    public ResponseEntity<UserDTO> fetchUserById(@PathVariable long id){
        return ResponseEntity.ok(userService.getUserById(id));
    }

    @PostMapping("/users")
    @Operation(description = "Create new User")
    public ResponseEntity<UserDTO> createUser(@RequestBody UserCreateRequest request){
        return ResponseEntity.ok(userService.createUser(request));
    }

    @PutMapping("/users")
    @Operation(description = "Update User")
    public ResponseEntity<UserDTO> updateUser(@RequestBody UserUpdateRequest request){
        return ResponseEntity.ok(userService.updateUser(request));
    }

    @DeleteMapping("/users/{id}")
    @Operation(description = "Delete User by Id")
    public ResponseEntity<UserDTO> deleteUser(@PathVariable long id){
        return ResponseEntity.ok(userService.deleteUser(id));
    }
}
