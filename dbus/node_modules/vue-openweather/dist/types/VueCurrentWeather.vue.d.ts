declare const _default: import("vue").DefineComponent<{
    apiKey: StringConstructor;
    lat: StringConstructor;
    long: StringConstructor;
    units: {
        type: StringConstructor;
        default: string;
    };
}, () => void, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, "currentWeather"[], "currentWeather", import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{
    apiKey: StringConstructor;
    lat: StringConstructor;
    long: StringConstructor;
    units: {
        type: StringConstructor;
        default: string;
    };
}>> & {
    onCurrentWeather?: ((...args: any[]) => any) | undefined;
}, {
    units: string;
}>;
export default _default;
