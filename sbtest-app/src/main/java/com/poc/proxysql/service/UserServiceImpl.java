package com.poc.proxysql.service;

import com.poc.proxysql.models.UserCreateRequest;
import com.poc.proxysql.models.UserDTO;
import com.poc.proxysql.models.UserUpdateRequest;
import com.poc.proxysql.repository.UserRepository;
import com.poc.proxysql.repository.entity.UserEntity;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author dipanjal
 * @since 0.0.1
 */

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final UserMapper mapper;

    @Override
    public List<UserDTO> getAllUsers() {
        return mapper.mapToDto(userRepository.findAll());
    }

    @Override
    public UserDTO getUserById(long id) {
        return userRepository.findById(id)
                .map(mapper::mapToDto)
                .orElseThrow(() -> new RuntimeException("User Not Found"));
    }

    @Override
    public UserDTO createUser(UserCreateRequest request) {
        UserEntity entity = userRepository.save(
                mapper.mapToEntity(request)
        );
        return mapper.mapToDto(entity);
    }

    @Override
    public UserDTO updateUser(UserUpdateRequest request) {
        UserEntity entity = userRepository.save(
                mapper.mapToEntity(userRepository
                        .findById(request.getId())
                        .orElseThrow(() -> new RuntimeException("Updatable User Not Found")),
                        request
                )
        );
        return mapper.mapToDto(entity);
    }

    @Override
    public UserDTO deleteUser(long id) {
        UserEntity entityToDelete = userRepository
                .findById(id)
                .orElseThrow(() -> new RuntimeException("User Not Found to Delete"));
        userRepository.delete(entityToDelete);
        return mapper.mapToDto(entityToDelete);
    }
}
