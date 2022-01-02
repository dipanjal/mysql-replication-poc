package com.poc.proxysql.repository;

import com.poc.proxysql.repository.entity.UserEntity;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * @author dipanjal
 * @since 0.0.1
 */

public interface UserRepository extends JpaRepository<UserEntity, Long> {
}
