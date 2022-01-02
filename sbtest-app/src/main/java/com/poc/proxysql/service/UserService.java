package com.poc.proxysql.service;


import com.poc.proxysql.models.UserCreateRequest;
import com.poc.proxysql.models.UserDTO;
import com.poc.proxysql.models.UserUpdateRequest;

import java.util.List;

public interface UserService {
    List<UserDTO> getAllUsers();
    UserDTO getUserById(long id);
    UserDTO createUser(UserCreateRequest request);
    UserDTO updateUser(UserUpdateRequest request);
    UserDTO deleteUser(long id);
}
