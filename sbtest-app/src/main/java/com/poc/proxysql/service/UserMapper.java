package com.poc.proxysql.service;

import com.poc.proxysql.models.UserCreateRequest;
import com.poc.proxysql.models.UserDTO;
import com.poc.proxysql.models.UserUpdateRequest;
import com.poc.proxysql.repository.entity.UserEntity;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.stream.Collectors;

/**
 * @author dipanjal
 * @since 0.0.1
 */

@Component
public class UserMapper {

    public UserDTO mapToDto(UserEntity entity) {
        return UserDTO.builder()
                .id(entity.getId())
                .name(entity.getName())
                .build();
    }

    public List<UserDTO> mapToDto(List<UserEntity> entities){
        return entities
                .stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    public UserEntity mapToEntity(UserCreateRequest request){
        UserEntity entity = new UserEntity();
        entity.setName(request.getName());
        return entity;
    }

    public UserEntity mapToEntity(UserEntity entity, UserUpdateRequest request){
        entity.setName(request.getName());
        return entity;
    }
}
