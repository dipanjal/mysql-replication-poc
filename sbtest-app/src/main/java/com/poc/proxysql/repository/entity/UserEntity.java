package com.poc.proxysql.repository.entity;

import lombok.Data;
import javax.persistence.*;

/**
 * @author dipanjal
 * @since 0.0.1
 */

@Entity
@Table(name = "users")
@Data
public class UserEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    private String name;
}
