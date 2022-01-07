package com.poc.proxysql.models;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

/**
 * @author dipanjal
 * @since 0.0.1
 */

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class UserUpdateRequest {
    private long id;
    private String name;
}
