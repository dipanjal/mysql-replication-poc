package com.poc.proxysql.models;

import lombok.Getter;
import lombok.Setter;

/**
 * @author dipanjal
 * @since 0.0.1
 */

@Getter
@Setter
public class UserUpdateRequest {
    private long id;
    private String name;
}
